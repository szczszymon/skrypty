function Ustaw(){
    for (let elem of document.querySelectorAll(".azure")){
        elem.style.backgroundColor = "azure";
        elem.style.boxShadow = "0 0 3px 0.5mm #A8A8A8";
        elem.style.border = "1px solid black";
        elem.style.margin = "12px";
    }// for azure

    for (let elem of document.querySelectorAll(".left")){
        elem.style.float = "left";
    }// for azure

    for (let elem of document.querySelectorAll(".right")){
        elem.style.float = "right";
    }// for azure

    for (let elem of document.querySelectorAll(".cLeft")){
        elem.style.clear = "left";
    }// for azure

    for (let elem of document.querySelectorAll(".cBoth")){
        elem.style.clear = "both";
    }// for azure

    for (let elem of document.getElementsByTagName("a")){
        elem.style.fontSize = "2vw";
    }// for a

    for (let elem of document.getElementsByTagName("h1")){
        elem.style.margin = "5px auto";
        elem.style.fontSize = "3.5vw";
    }// for azure

    let elem = document.getElementsByTagName("header")
        elem.style.paddingLeft = "10px";
        elem.style.height = "auto";
        elem.style.backgroundColor = "#EFF";
        elem.style.borderColor = "#A8A8A8";

    elem = document.getElementsByTagName("nav")
        elem.style.padding = "10px 15px 10px 20px";
        elem.style.height = "auto";
        elem.style.width = "auto";

    elem = document.getElementsByTagName("aside")
        elem.style.padding = "0 16.5% 10px 10px";
        elem.style.width = "auto";

    elem = document.getElementsByTagName("main")
        elem.style.padding = "10px 0 15px 12px";

    elem = document.getElementsByTagName("blockquote")
        elem.style.marginLeft = "0";
        elem.style.marginRight = "5px";
        elem.style.fontSize = "1.5vw";

    elem = document.getElementsByTagName("footer")
        elem.style.padding = "10px";
        elem.style.height = "auto";
}// Ustaw()

function Skasuj() {
    for (let elem of document.querySelectorAll(".all")){
        elem.style = "";
    }//for all
}// Skasuj()