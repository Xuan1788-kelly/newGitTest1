var item1 = document.getElementById("Italy1");
var item2 = document.getElementById("Italy2");
var item3 = document.getElementById("Italy3");


item1.addEventListener("click", picLink);
item2.addEventListener("click", picLink);
item3.addEventListener("click", picLink);

function picLink() {
    var allImages = document.querySelectorAll("img");

    for (var i = 0; i < allImages.length; i++) {
        allImages[i].className = "hide";
    }

    var picId = this.attributes["data-image"].value;
    var pic = document.getElementById(picId);
    if (pic.className == "hide") {
        pic.className = "";
    } else {
        pic.className = "hide";
    }
};