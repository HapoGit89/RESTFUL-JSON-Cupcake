let input = document.querySelector('#input')
let cupcakes = document.querySelector('#cupcake-output')





async function getCupcakes(){
   resp = await axios.get('/api/cupcakes')
   return resp.data
}

async function postCupcake(){
    flavor = document.querySelector('#flavor').value
    size = document.querySelector('#size').value
    rating= document.querySelector('#rating').value
    image = document.querySelector('#image_url').value
    if (image === ""){
        resp = await axios.post('/api/cupcakes', {"flavor": flavor, "size": size, "rating": rating} )}
    else {
        resp = await axios.post('/api/cupcakes', {"flavor": flavor, "size": size, "rating": rating, "image" : image} )}
    return resp.data
}

async function onStart(){
    resp =await getCupcakes()
    console.log(resp.cupcakes)
    for (let cake of resp.cupcakes){
        const newUl = document.createElement("ul")
        const newImg = document.createElement("img")
        const newFlav = document.createElement("li");
        const newSize = document.createElement("li");
        const newRating = document.createElement("li");
        newImg.src = cake.image
        newImg.classList.add("thumbnail")
        newFlav.innerText = `Flavor: ${cake.flavor}`
        newSize.innerText = `Size: ${cake.size}`
        newRating.innerText = `Rating: ${cake.rating}`
        newUl.appendChild(newImg)
        newUl.appendChild(newFlav)
        newUl.appendChild(newSize)
        newUl.appendChild(newRating)
        cupcakes.appendChild(newUl)
    }
}

onStart()


input.addEventListener('submit', async function(e){
    e.preventDefault()
    await postCupcake()
    console.log("This form was submitted")
    onStart()
})
