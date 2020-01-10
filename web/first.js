function mouseOver() {
    let btn = document.getElementById("btn");
    btn.style.top = (Math.random() * 300) + "px";
    btn.style.left = (Math.random() * 600) + "px";
}

function btnOnClick() {
    window.location.href = "D:\\workspace\\internet_engineering_projects\\web\\second.html"
}

document.getElementById("btn").onmouseover = function() { mouseOver(); }
document.getElementById("btn").onclick = function() { btnOnClick(); }