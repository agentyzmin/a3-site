/**
 * Created by knyshv on 2/24/17.
 */
$(window).resize(function () {
    featured_image_resize();
});

$(document).ready(function () {
    featured_image_resize();
})

var featured_image_resize = function () {
    var image_height = document.getElementById("featured-image").clientHeight;
    var feature_image_height = Math.min(350, image_height * 0.6);
    var margin_top = 0;
    if (feature_image_height < image_height){
        margin_top = (feature_image_height - image_height) * 0.4;
        document.getElementById("featured-image").style.marginTop = margin_top + "px";
    }
}
