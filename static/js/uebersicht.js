

var karten = $(".karte")

karten.mouseenter(function() {
    $(this).querySelector('h2').css("color: grey;")
})

karten.mouseleave(function() {
   $(this).querySelector('h2').css("color: white;")
})

