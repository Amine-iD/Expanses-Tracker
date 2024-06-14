function loadData(itemData , categoryData){
    items = JSON.parse(itemData)
    categories = JSON.parse(categoryData)
}

function addRow(){
        let newRow = '<td class="mr-5"  title="Description"> <textarea name="Description" id="xpanse-description"></textarea></td><td class="mr-5" ><select name="item" id="item">'
    // Adding the <td> of items
    for(i=0 ; i<items.length ; i++){
        newRow += `<option value="${items[i]}">` +items[i]+ '</option>'
    }
    // Adding the <td> of categories
        newRow+= '</select></td><td class="mr-5" ><select name="item" id="item">'
    for(i=0 ; i<categories.length ; i++){
        newRow += `<option value=" ${categories[i]}  ">` +categories[i]+'</option>'
        }
    
    newRow += '</select></td><td class="mr-5" ><input type="date" name="" id=""></td>'
    
    const tbody = document.querySelector(".exp-table tbody")//when I did it using the id of the table it didn't stay working for too long!!
    // const tbody = document.querySelector('#expansesTable tbody')
    let tr = document.createElement('tr')
    tr.className = 'hover:bg-green-300'
    tr.innerHTML = newRow
    tbody.appendChild(tr)
    // $(".exp-table tbody").append(newRow)   !!!!!!!!!------This has a weird behaviour-------!!!!!!!!!!!
}
function selectRow(){

}


function deleteRow(){
    /** This is the simplest form of a delete() function , but it lacks precision=>{which row to delete!} */
    let row = document.querySelector('tbody').lastChild
    row.remove()
}