$(document).ready(function(){
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/?search_filter=' + searchText,
            type: 'GET',
            success: function(resp){
                var newHtml = resp.data.map(d => {
                    return `<div class="well category"> 
                            <a href="/product/${d.id}"> 
                            <img src ="${d.image}" />
                            <h4>${d.name}</h4>
                            <p>${d.description}</p>
                            
                            </a>
                        </div>`
                });
                $('.firesale').html(newHtml.join(''));
                $('#search-box').val('');
            },
// TODO: bæta við price fyrir ofan..
            error: function(xhr, status, error){
                // TODO: show toastr
                console.error(error);
        }
        })
    });
});

//þarf að gera get request fyrir að ná í allt og svo nota það url með search filter.
//þarf að finna réttan stað (view) til að setja það get request inn.
//SP. TA: við erum með öðruvísi til að fá allt upp (því við skiptum í catagoríur stax),
// er samt ekki í lagi að búa til ajax req líka?