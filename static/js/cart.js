


$(document).ready(function() {
    $(".increment-btn").click(function(e){
        e.preventDefault();

        
        
        var productId = $(this).closest(".product_data").find(".guest-user-product-id").val()
        
        var totalQuantity = $(this).closest(".product_data").find(".guest-user-product-quantity").val()
        var price = $(this).closest(".product_data").find('#selling_price').text()
        var inc_value =  $(this).closest(".product_data").find('.qty-input').val();
        var value = parseInt(inc_value,10);


        value = isNaN(value) ? 0: value;
        if(totalQuantity > value){
            value++
            console.log("HHHHhh")
            if(user == 'AnonymousUser'){
            cart[productId]["quantity"] = parseInt(value)
            document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
          
            }
            var total = value * price
            $(this).closest(".product_data").find('.qty-input').val(value);
            $(this).closest(".product_data").find('#item-total').text("$"+total);
            
            
            console.log(totalQuantity)
        }else if (value >= totalQuantity){
            alertify.error("Out of Stock")
        }

    })

    $(".decrement-btn").click(function(e){
        e.preventDefault();

        
        var productId = $(this).closest(".product_data").find(".guest-user-product-id").val()
        var price = $(this).closest(".product_data").find('#selling_price').text()
        var dec_value =  $(this).closest(".product_data").find('.qty-input').val();
        var value = parseInt(dec_value,10);
        value = isNaN(value) ? 0: value;
       
        if(value > 1){
            value--
            
            if(user == 'AnonymousUser'){
            cart[productId]["quantity"] = parseInt(value)
            document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
            console.log(cart)
            }
            var total = value * price
            $(this).closest(".product_data").find('.qty-input').val(value);
            $(this).closest(".product_data").find('#item-total').text("$"+total);
           
           
        }
        

    })

    // $(".addToCartBtn").click(function(e){
    //     e.preventDefault();

    //     var product_id = $(this).closest('product_data').find('.prod_id').val();
    //     var product_qty = $(this).closest('product_data').find('.qty-input').val();
    //     var token = $('input[name=csrfmiddlewaretoken]').val()

    //     console.log(product_id);
    //     $.ajax({
    //         method: "POST",
    //         url: "/add-to-cart",
    //         data: {
    //             product_id: product_id,
    //             product_qty: product_qty,
    //             csrfmiddlewaretoken: token
    //         },
    //         dataType: "dataType",
    //         success: function(response){
    //             console.log(response)
    //         }
    //     })

    // })

    $(".changeQuantity").click(function(e){
        e.preventDefault();

        var totalQuantity = $(this).closest(".product_data").find(".guest-user-product-quantity").val()
        var product_id = $(this).closest('.product_data').find('input[name = product_id]').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val()
        var action = $(this).data('action');
        
        if(user == 'AnonymousUser'){
            cart[product_id]["quantity"] = parseInt(product_qty)
            document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
            console.log(cart)
            return
            }
        console.log(action)
        $.ajax({
            method: "POST",
            url: "/shop/cart/update-cart",
            data: {
                "product_id": product_id,
                "product_qty": product_qty,
                "action": action,
                csrfmiddlewaretoken: token
            },
            dataType: "json",
            success: function(response){
                if(response.value){
                $('#lblCartCount').html(response.num_of_items)
                }
                console.log(response)
                $('.guest-user-product-quantity').val(response.product_quantity)
                console.log(totalQuantity)
                
            }
        })

    })

    $(document).on('click','.delete-cart-item',function(e){
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('input[name = product_id]').val();
        
        var token = $('input[name=csrfmiddlewaretoken]').val()

        console.log(token)
        console.log(product_id);
        if(user == "AnonymousUser"){
            delete cart[product_id]
            document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
            $('.cart-data').load(location.href + " .cart-data" )
            console.log(cart)
            return
        }
        $.ajax({
            method: "POST",
            url: "/shop/cart/delete_cart",
            data: {
                "product_id": product_id,
                
                csrfmiddlewaretoken: token
            },
           
            success: function(response){
                console.log(response)
                $('.cart-data').load(location.href + " .cart-data" )
            }
        })

    })

    $('.addToWishlist').click(function (e){
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('input[name = product_id]').val();
        var token = $('input[name=csrfmiddlewaretoken]').val()
        
        $.ajax({
            method: "POST",
            url: "/shop/add-to-wishlist",
            data: {
                "product_id": product_id,
                
                csrfmiddlewaretoken: token
            },
            

            success: function(response){
                console.log(response)
                alertify.success(response.status)
               
            }
        })
    })

    $(document).on('click','.delete-wishlist-item',function(e){
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('input[name = product_id]').val();
        
        var token = $('input[name=csrfmiddlewaretoken]').val()

        console.log(token)
        console.log(product_id);
      
        $.ajax({
            method: "POST",
            url: "/shop/cart/delete_wishlist",
            data: {
                "product_id": product_id,
                
                csrfmiddlewaretoken: token
            },
           
            success: function(response){
                console.log(response)
                $('.wishlist-data').load(location.href + " .wishlist-data" )
            }
        })

    })

    $(document).on('click','.activate-address',function(e){
        e.preventDefault();
    
        var _aid = $(this).attr('data-address')
        var _vm = $(this);
        
     
      
        $.ajax({
        
            url: "/activate-address",
            data: {
                
                "id": _aid,
            },
            dataType : 'json',
            beforeSend:function(){
                _vm.attr('disabled', true)
            },
           
            success: function(response){
                if (response.bool == true){
                    $('.address-change').load(location.href + " .address-change" )
                    
                    
                   
                }
               
            }
        })
    
    })

  
})


   



// var updateBtns = document.getElementsByClassName('update-cart')


// for(var i = 0; i < updateBtns.length; i++){
//     updateBtns[i].addEventListener('click',function(){
//         var productId = this.dataset.product
//         var action = this.dataset.action
        
        
//         console.log('productId',productId, 'action',action)

//         console.log(user)

//         if(user=='AnonymousUser'){
//             console.log("Not logged In")

//         }else{
//             updateUserOrder(productId, action)
//         }
//     })
// }

// function updateUserOrder(productId, action){
//     console.log("user is logged in ")

//     var url = "cart/update_item/"

//     fetch(url, {
//         method : "POST",
//         headers:{
//             'Content-Type':'application/json',
//             'X-CSRFToken':csrftoken,
//         },
//         body: JSON.stringify({'productId':productId, 'action':action})
        
//     })
//     .then((response) =>{
//         return response.json()
//     })

//     .then((data) =>{
//         document.getElementById("lblCartCount").innerHTML = data
//         console.log(data)
        
        
//     })
// }

  
// function refreshDiv(){
//     $('#cart-div-change').load(location.href + "#cart-div-change")
// }

//   function reloadDiv() {
//     $.ajax({
//         url: "cart/my_view/",
//         type: "GET",
//         dataType: "json",
//         success: function(data) {
            
//             // update the content of the div with the new data
//             $("#cart-div-change").html(data.html);
//         },
//         error: function(xhr, status, error) {
//             console.log("An error occurred while loading the div.");
//         }
//     });
// }