# -*- coding: utf-8 -*-
import os
from flask import Flask, request, url_for, send_from_directory
from werkzeug.utils import secure_filename
from MyQR import myqr
import re

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd()
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>漂亮的动态二维码制作小工具</title>
</head>

<body>
<fieldset>
    <legend>来制作你的漂亮高端大气动态二维码吧</legend>
<form method="post" enctype="multipart/form-data">
    <table border="1" bordercolor="#0099ff" cellpadding="10px" cellspacing="0">
        <tr>
            <th colspan="3">制作页面</th>
        </tr>

        <tr>
            <td>转化的文本</td>
            <td>
                <input  type="text" name="tom1"/>
            </td>
            <td><font color="#FF0000">--请输入要转换的文本--</font></td>
        </tr>
		<tr>
            <td>转换的链接</td>
            <td>
                <input  type="url" name="tom2"/>
            </td>
            <td><font color="#FF0000">--请输入要转换的链接，和文本二选一--</font></td>
        </tr>
        <tr>
            <td>是否彩色：</td>
            <td>
                <input type="radio" name="sex" value="True" checked="checked"/>是
                <input type="radio" name="sex" value="False" />否
            </td>
            <td><font color="#FF0000">*彩色的当然好看一点了</font></td>
        </tr>
        <tr>
            <td>选择纠错等级：</td>
            <td>
                <select name="level"/>
                    <option value="L">---选择纠错等级---</option>
                    <option value="L">L</option>
                    <option value="M">M</option>
                    <option value="Q">Q</option>
                    <option value="H">H</option>
            </td>
            <td><font color="#FF0000">*选择自己想要的纠错等级</font></td>
        </tr>
        <tr>
            <td>选择背景图片：</td>
            <td>
				<input type=file name=file>
            </td>
            <td><font color="#FF0000">如果想要彩色背景可以自定义选择</font></td>
        </tr>
        <tr>
            <th colspan="1">
                <input type="submit" value="提交" /></a>
            </th>
        </tr>
    </table>
</form>
</fieldset>
</body>
</html>'''
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        words = request.form['tom1']
        Level = request.form['level']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            version, level, qr_name = myqr.run(
                words,
                version=1,
                level=Level,
                picture=filename,
                colorized=True,
                contrast=1.0,
                brightness=1.0,
                save_name=None,
                save_dir=os.getcwd()
            )
            print(qr_name)
            print(Level)
            qr_name = re.search(r".+\\(.+)$",qr_name)
            qr_name1 = qr_name.group(1)
            print(qr_name.group(1))
            print(filename)
            file_url = url_for('uploaded_file', filename=qr_name1)
            return html + \
                   '<fieldset><legend>叮叮当当！！！</legend>'+\
                   '<table><tr><td>结果效果图：</td><td><img src=' + file_url +\
                   '>' +'<td>' +'<td><font color="#FF0000">'+words+'</font></td></tr></table>'+\
                   '</fieldset>'
    return html


if __name__ == '__main__':
    app.run()
