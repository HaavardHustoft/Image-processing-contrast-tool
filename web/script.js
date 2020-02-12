var img = document.getElementById('transformed')
var histogram = document.getElementById('histogram')


var loadFile = function(event){
    var image = document.getElementById('output');
    image.src= URL.createObjectURL(event.target.files[0]);
};