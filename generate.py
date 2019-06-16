# -*- coding:utf-8 -*-

import pathlib

pictures = list(pathlib.Path('.').glob('*.png'))

steps = [
    ("0,0","0,1","Weiter"),
    ("0,1","0,2","Weiter"),
    ("0,2","0,3","Weiter"),
    ("0,3","0,4","Weiter"),
    ("0,4","0,5","Das Parlament verlassen"),
    ("0,5","1","Das Paket untersuchen"),
    ("1","2","Weiter"),
    ("2","3","Weiter"),
    ("3","4a","KAMPF"),
    ("4a","5,0","Strafzahlung"),
    ("5,0","5,5","Weiter"),
    ("5,5","5,7","Weiter"),
    ("5,7","4b","Weiter"),
    ("4b","6","Mindestlohn"),
    ("6","6,5","Weiter"),
    ("6,5","7","Weiter"),
    ("7","8","Weiter"),
    ("8","9","Weiter"),
    ("9","10","Weiter"),
    ("10","11","Gesetz"),
    ("11","12","Weiter"),
    ("12","13","Weiter"),
    ("13","14","Weiter"),
    ("14","15","Weiter"),
    ("15","16","Weiter"),
    ("16","17","Weiter"),
    ("17","18","Weiter"),
    ("18","19","Lange Rede"),
    ("19","20","Weiter"),
    ("20","21","Neuland"),
    ("21","22","Neuland"),
    ("22","23","Weiter"),
    ("23","24","Weiter"),
    ("24","25","Weiter"),
    ("25","26","Weiter"),
    ("26","27","Weiter"),
    ("27","28","Weiter"),
    ("28","29","Weiter"),
    ("29","30","Weiter"),
    ("30","31","Weiter"),
    ("31","32","Weiter"),
    ("32","33","Artikel 13"),
    ("33","34","Weiter"),
    ("34","35","Weiter"),
    ("35","36","Weiter"),
    ("36","37","Weiter"),
    ("37","38","Weiter"),
    ("38","39","Weiter"),
    ("39","0,0","Neustart"),
    ]

template = """<!DOCTYPE html>
<html>
<head>
        <meta charset="utf-8"> 
    <title>EUmon im Neuland</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<!--AB HIER SICHTBAR-->
<body>
    <div style="width:440px;margin:0px auto"><img src="pokeball2.png" alt="pokeball" width="60" height="60"> <h1>EUmon im Neuland</h1>
        
    <a href="step_0,0.html"><h2>Spiel</h2></a>
    <a href="info.html"><h2>Info</h2></a>
    <a href="impressum.html"><h2>Impressum</h2></a>
        
    <img src="{picture}.png" alt="start" width="400" height="360">
    <a href="step_{next}.html"><h2>{text}</h2></a></div>

</body>
<!--AB HIER NICHT MEHR SICHTBAR-->

</html> """

for step in steps:
    picture,next,text = step
    html = template.format(picture = picture, next = next, text = text)
    pathlib.Path(f"step_{picture}.html").write_text(html)