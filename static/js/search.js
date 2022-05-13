$(document).ready(function(){
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/?search_filter=' + searchText,
            type: 'GET',
            success: function(resp){
                var newHtml = resp.data.map(d => {
                    return `<div class="col-sm-12 col-md-6 col-lg-4">
                                <a href="/product/${d.id}" class="text-decoration-none text-center"> 
                                    <div class="card card-box" id="well category"> 
                                        <img src="${d.image}" class="card-img-top prod-image" />
                                        <h4 class="card-title">${d.name}</h4>
                                    </div>
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

