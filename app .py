from flask import Flask

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Happy Birthday Diya ❤️</title>

<style>
body{
    margin:0;
    overflow:hidden;
    background:linear-gradient(135deg,#ff5f9e,#ffb6c1);
    font-family:Arial,sans-serif;
    text-align:center;
}

h1{
    color:white;
    margin-top:120px;
    font-size:60px;
    text-shadow:2px 2px 8px black;
}

h2{
    color:white;
    font-size:30px;
}

.balloon{
    position:absolute;
    bottom:-120px;
    width:70px;
    height:90px;
    border-radius:50%;
    animation:float linear infinite;
}

.balloon::after{
    content:"";
    position:absolute;
    width:2px;
    height:70px;
    background:white;
    left:34px;
    top:90px;
}

@keyframes float{
    from{transform:translateY(0);}
    to{transform:translateY(-120vh);}
}

@keyframes pop{
    0%{transform:scale(1);opacity:1;}
    100%{transform:scale(3);opacity:0;}
}
</style>

</head>

<body>

<h1>🎉 Happy Birthday Diya ❤️ 🎉</h1>

<h2>You Are My Love Forever 💖</h2>

<script>

const colors=[
"red","blue","green","yellow",
"purple","orange","pink","cyan"
];

for(let i=0;i<50;i++){

let b=document.createElement("div");

b.className="balloon";

b.style.background=
colors[Math.floor(Math.random()*colors.length)];

b.style.left=Math.random()*100+"vw";

b.style.animationDuration=
(4+Math.random()*5)+"s";

document.body.appendChild(b);

setTimeout(()=>{
b.style.animation="pop 1s forwards";
},4000+Math.random()*3000);

}

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return HTML

if __name__ == "__main__":
    app.run(debug=True)
