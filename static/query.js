$(function(){
    var $sets = $('#sets');
    $.ajax({
        type: 'GET',
        url: 'http://api.mtgapi.com/v2/sets', 
        success: function(sets){ 
            $.each(sets, function(i, set) {
                console.write(set.name);
                $sets.append('<li>' + set.name + '</li>');
            });
        },
        error: function(){
            alert("ajax error"); 
        }
    });
});
