onload = function () {
    var arr = document.getElementsByClassName("slide");
    for (var i = 0; i < arr.length; i++) {
        arr[i].style.left = i * 416 + "px";
    }
};

function LeftMove() {
    var arr = document.getElementsByClassName("slide");//获取三个子li
    for (var i = 0; i < arr.length; i++) {
        var left = parseFloat(arr[i].style.left);
        left -= 2;
        var width = 416;//图片的宽度
        if (left <= -width) {
            left = (arr.length - 1) * width;//当图片完全走出显示框，拼接到末尾
            clearInterval(moveId);
        }
        arr[i].style.left = left + "px";
    }
}

function divInterval() {
    moveId = setInterval(LeftMove, 10);//毫秒定时器
}
timeId = setInterval(divInterval, 2000);//秒定时器。

function stop() {
    clearInterval(timeId);
}

function start() {
    clearInterval(timeId);
    timeId = setInterval(divInterval, 2000);
}

//页面失去焦点停止
onblur = function () {
    stop();
};
//页面获取焦点时开始
onfocus = function () {
    start();
};
