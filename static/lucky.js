/** processForm: get data from form and make AJAX call to our API. */


async function processForm(evt) {
    evt.preventDefault()
    const name = $('#name').val()
    const year = $('#year').val()
    const email = $('#email').val()
    const color = $('#color').val()
    
    result = await axios.post('/api/get-lucky-num', {name, year, email, color})
    // result = await axios.post('/api/get-lucky-num')
    console.log("result is", result)
   
    handleResponse(result)
}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(resp) {
    if (resp.data["errors"]){
        errorDict = resp.data["errors"]
        for (let i =0; i < Object.keys(errorDict).length; i++){
        errName = Object.keys(errorDict)[i]
        errText = resp.data["errors"][errName]
        console.log("errname is", errName, "and errtext is ",errText)
        $(`#${errName}-err`).html(errText)
        }
    }
    else{
    let randNum = resp.data["num"]["num"]
    let randFact = resp.data["num"]["fact"]
    let year = resp.data["year"]["year"]
    let yearFact = resp.data["year"]["fact"]
    
    $("#lucky-results").append(`<div>"Your lucky number is 
    ${randNum} (${randFact})</div><div>Your birth year(${year}) 
    fact is ${yearFact})</div>`)
    }
}

$("#lucky-form").on("submit", processForm);



// async function processForm(evt) {
//     handleResponse(resp, year, respYear)

//     result = await axios.post('/api/get-lucky-num')
    
//     result === {data:{}}

//     create
//     result['errors'][error_name] = error
// }



// $("#lucky-form").on("submit", processForm);
