var square_x = 5;
var square_y = 50;
var square_size = 20;

var draw = function() {
    background(255, 0, 0);
    rect(square_x, square_y, square_size, square_size);
    square_x += 1;
};
