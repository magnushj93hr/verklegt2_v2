$(document).ready(function(){
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('search-box').val();
        $.ajax({
            url: '' + searchText,
            type: 'GET',
            success: function(resp){
                //Klára hér!
            },
            error: function(xhr, status, error){
                console.error(error);
        }
        })
    });
});

//þarf að gera get request fyrir að ná í allt og svo nota það url með search filter.
//þarf að finna réttan stað (view) til að setja það get request inn.
//SP. TA: við erum með öðruvísi til að fá allt upp (því við skiptum í catagoríur stax),
// er samt ekki í lagi að búa til ajax req líka?