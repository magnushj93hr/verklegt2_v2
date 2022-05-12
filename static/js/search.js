$(document).ready(function(){
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/?search_filter=' + searchText,
            type: 'GET',
            success: function(resp){
                var newHtml = resp.data.map(d => {
                    return `<div id="well category"> 
                            <a href="/product/${d.id}"> 
                            <img src ="${d.image}" />
                            <h4>${d.name}</h4>
                            <p>${d.description}</p>
                            
                            </a>
                        </div>`
                });
                $('#firesale').html(newHtml.join(''));
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

