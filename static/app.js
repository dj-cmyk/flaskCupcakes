console.log('connected');

const BASE_URL = "http://127.0.0.1:5000/"


const $cupcakeList = $(".cupcake-list");
const $cupcakeForm = $("#cupcake-form");
const $formSubmitBtn = $(".cupcake-btn");



$(document).ready(getCupcakeList);


async function getCupcakeList(){
    const cupcakes = await axios({
        url: `${BASE_URL}/api/cupcakes`,
        method: "GET"
    })
    for (let cupcake of cupcakes.data.cupcakes) {
        let cupcakeHtml = generateCupcakeListHTML(cupcake)
        $cupcakeList.append(cupcakeHtml)
    } 
}

function generateCupcakeListHTML(item){
    const htmlString = `<li data-id=${item.id}>${item.flavor} - ${item.size} - ${item.rating} <button class="badge badge-info edit-btn">edit</button><button class="badge badge-warning delete-btn">delete</button></li>`
    return htmlString
}


async function addCupcake(evt) {
    evt.preventDefault();
  
    // get the values from the form
    const flavor = $("#flavor").val();
    const size = $("#size").val();
    const rating = parseFloat($("#rating").val());
    const image = $("#image").val();

    // send new cupcake info to api as post request
    const new_cupcake = await axios({
        url: `${BASE_URL}/api/cupcakes`,
        method: "POST",
        data: {
            "flavor":flavor, 
            "size":size, 
            "rating":rating, 
            "image":image
        }
    })

    // take response from api and generate a new cupcake li to add to DOM
    const newCakeHTML = generateCupcakeListHTML(new_cupcake.data.cupcake)
    $cupcakeList.append(newCakeHTML)
    
    // reset the form
    $cupcakeForm.trigger("reset");
  }
  
$cupcakeForm.on("submit", addCupcake);



async function deleteCupcake(){
    const id = $(this).parent().data('id');
    await axios.delete(`/api/cupcakes/${id}`);
    $(this).parent().remove()
}

$cupcakeList.on( "click", ".delete-btn", deleteCupcake);
