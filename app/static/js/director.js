/* director.js - Theatre blocking JavaScript */
"use strict";
console.log('director.js') // log to the JavaScript console.

// At first, no script is on the screen, so we set blockShown false
var blockShown = false;
/* UI functions below - DO NOT change them */

// Function to remove all blocking parts from current window
function removeAllBlocks() {
	blocks.innerHTML = '';
	setScriptNumber('');
}

/* This function returns a JavaScript array with the information about blocking displayed
in the browser window.*/
function getBlockingDetailsOnScreen() {
	
	// this array will hold 
	const allBlocks = []

	// go through all of the script parts and scrape the blocking informatio on the screen
	for (let i = 0; i < blocks.children.length; i++) {
		const block = {};  const blockElement = blocks.children[i]
		block.part = i + 1;
		block.text = blockElement.children[1].textContent;
		block.actors = []
		const actors = blockElement.children[2].children
		for (let j = 0; j < actors.length; j++) {
			block.actors.push([actors[j].textContent, actors[j].children[0].value])
		}
		allBlocks.push(block)
	}

	// Look in the JavaScript console to see the result of calling this function
	return allBlocks;
}

function setScriptNumber(num) {
	const scriptNum = document.querySelector('#scriptNum')
	scriptNum.innerHTML = `${num}`
}

function getScriptNumber(num) {
	return document.querySelector('#scriptNum').innerHTML
}

/* Function to add the blocking parts to browser window */
function addBlockToScreen(scriptText, startChar, endChar, actors, positions) {

	const scriptPartText = scriptText.slice(startChar, endChar + 1);
	const html = `<h4>Part ${blocks.children.length + 1}</h4>
      <p><em>"${scriptPartText}"</em></p>
      <div class='actors'></div>`

    const block = document.createElement('div')
    block.className = 'col-lg-12'
    block.innerHTML = html;
    for (let j = 0; j < actors.length; j++) {
    	const actorHtml = `${actors[j]}<input id='scriptText' style="width: 40px;" type="text" name="" value="${positions[j]}">`
    	const actorContainer = document.createElement('p');
    	actorContainer.innerHTML = actorHtml;
    	block.children[2].appendChild(actorContainer)
	} 

    console.log(block)
    blocks.appendChild(block)

}

/* UI functions above */


// Adding example script blocking 
// (the blocks should be removed from the screen when getting a script from the server)
// addBlockToScreen(`That's it Claudius, I'm leaving!Fine! Oh..he left already..`, 0, 31, ['Hamlet', 'Claudius'], [5, 2])
// addBlockToScreen(`That's it Claudius, I'm leaving!Fine! Oh..he left already..`, 32, 58, ['Hamlet', 'Claudius'], ['', 3])
// setScriptNumber('example')

//////////////
// The two functions below should make calls to the server
// You will have to edit these functions.

function getBlocking() {
	// Check if the users provide a valid script number.
	if(document.getElementById("scriptNumText").value === "") {
		alert("Please input a valid Script Number!")
		return
	}
	removeAllBlocks();
	const scriptNumber = scriptNumText.value;
	setScriptNumber(scriptNumber)
	console.log(`Get blocking for script number ${scriptNumber}`)

	console.log('Getting ')
	/// Make a GET call (using fetch()) to get your script and blocking info from the server,
	// and use the functions above to add the elements to the browser window.
	// (similar to actor.js)


	const url = '/script' + '/' + scriptNumber

	// A 'fetch' AJAX call to the server.
    fetch(url)
    	.then((res) => { 
    		//// Do not write any code here
	        return res.json()
	        //// Do not write any code here
	    })
	    .then((jsonResult) => {
	    	// This is where the JSON result (jsonResult) from the server can be accessed and used.
	        console.log('Result:', jsonResult)
			// Use the JSON to add a script part
			// We are going to visit every part of the script. ASSUME that the part number is consecutive.
			for(let k = 0; k < jsonResult.length; k++) {
				let script = jsonResult[k];
				let blockingInfo = script[3];
				let listOfActorNames = [];
				let listofActorPositions = [];
				for(let index in blockingInfo) {
					listOfActorNames.push(blockingInfo[index][0]);
					listofActorPositions.push(blockingInfo[index][1]);
				  }
				addBlockToScreen(script[0], parseInt(script[1]), parseInt(script[2]), listOfActorNames, listofActorPositions)
			}

			blockShown = true;
	    }).catch((error) => {
	    	// if an error occured it will be logged to the JavaScript console here.
	        console.log("An error occured with fetch:", error)
		})

}

function changeScript() {
	// You can make a POST call with all of the 
	// blocking data to save it on the server

	// If the user tries to add an actor before he / she gets the script on screen, we will give the user an alert.
	if(blockShown != true) {
		alert("Please input a Get the Script Blocking first!")
		return
	}

	var elements = document.querySelectorAll('[id=scriptText]');

	for (var i = 0; i < elements.length; i++) {
		let element = elements[i]
		var numbers = /^[0-9]+$/;
		if ( !(element.value.match(numbers)) || parseInt(element.value) < 0 || parseInt(element.value) > 8) {
			alert("Only 0 - 8 is accepted!")
			return
		}
	}


	const url = '/script';

    // The data we are going to send in our request
    // It is a Javascript Object that will be converted to JSON
    let data = {
    	scriptNum: getScriptNumber(),
		// What else do you need to send to the server?    
		blocks: getBlockingDetailsOnScreen()
    }

    // Create the request constructor with all the parameters we need
    const request = new Request(url, {
        method: 'post', 
        body: JSON.stringify(data),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
    });

    // Send the request
    fetch(request)
    	.then((res) => { 
    		//// Do not write any code here
    		// Logs success if server accepted the request
    		//   You should still check to make sure the blocking was saved properly
    		//   to the text files on the server.
    		console.log('Success') 
	        return res.json()
	        ////
	    })
	    .then((jsonResult) => {
	    	// Although this is a post request, sometimes you might return JSON as well
	        console.log('Result:', jsonResult)

	    }).catch((error) => {
	    	// if an error occured it will be logged to the JavaScript console here.
	        console.log("An error occured with fetch:", error)
	    })
}


function changeActor(option) {
	// You can make a POST call with all of the 
	// blocking data to save it on the server

	// Check if the users provide a valid actor name.
	if(document.getElementById("actorName").value === "") {
		alert("Please input a valid Actor Name!")
		return
	}


	// If the user tries to add an actor before he / she gets the script on screen, we will give the user an alert.
	if (blockShown != true) {
		alert("Please Get Script Blocking First!")
		return
	}
	const url = '/actor';

    // The data we are going to send in our request
    // It is a Javascript Object that will be converted to JSON
    let data = {
    	scriptNum: getScriptNumber(),
		// What else do you need to send to the server?    
		blocks: getBlockingDetailsOnScreen(),
		newActor: document.getElementById("actorName").value,
		type: option
	}
	

    // Create the request constructor with all the parameters we need
    const request = new Request(url, {
        method: 'post', 
        body: JSON.stringify(data),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
    });

    // Send the request
    fetch(request)
    	.then((res) => { 
    		//// Do not write any code here
    		// Logs success if server accepted the request
    		//   You should still check to make sure the blocking was saved properly
    		//   to the text files on the server.
			console.log('Success')
			getBlocking()
	        return res.json()
	        ////
	    })
	    .then((jsonResult) => {
	    	// Although this is a post request, sometimes you might return JSON as well
	        console.log('Result:', jsonResult)

	    }).catch((error) => {
	    	// if an error occured it will be logged to the JavaScript console here.
	        console.log("An error occured with fetch:", error)
	    })
}