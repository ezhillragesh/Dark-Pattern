/*global chrome*/
import React from 'react';
import './index.css';

function currentUrl() {
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    var activeTab = tabs[0];
    var activeTabUrl = activeTab.url;
    document.getElementById('url').value = activeTabUrl;
  });
}

function sentToserver(link){
  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");
  const raw = JSON.stringify({
  "link": link
});
console.log(link);

const requestOptions = {
  method: "POST",
  headers: myHeaders,
  body: raw,
  redirect: "follow"
};
  
fetch("https://dark-pattern.onrender.com/summary", requestOptions)
  .then(response => response.json())
  .then(data => {
    const summaryText = data.message.Summary;
    // const darkpatternText=data.message.TextManipulation;
    // console.log(summaryText);
    
    document.getElementById('txtComment').value = summaryText;
  })
  .catch(error => console.error(error));

}

fetch("https://dark-pattern.onrender.com/process_link", requestOptions)
  .then(response => response.json())
  .then(data => {
    // const summaryText = data.message.Summary;
    const darkpatternText=data.message.TextManipulation;
    // console.log(summaryText);
    document.getElementById('darkpattern').value=darkpatternText;
  })
  .catch(error => console.error(error));

}



function App() {
  const handleCheckNow = () => {
    const inputLink = document.getElementById('url').value;
    console.log(inputLink + " is the input link")
    sentToserver(inputLink);
  };

  return (
    <div className="flex justify-center items-center h-screen">
      <div className='flex flex-col items-center font-mono w-full ml-3 mr-3'>
        <label htmlFor="helper-text" className="block mb-2 text-sm font-bold text-black ">Page Link</label>
        <input type="url" id="url" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 mb-3" placeholder="Paste your web link" />

        <button type="button" className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-3 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800" onClick={handleCheckNow}>Check now!</button>
        <button type="button" className="focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 mb-3 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800" onClick={currentUrl}>Current URL</button>
        <textarea id="txtComment" placeholder="Your Privacy Summary will be shown here" className="h-100 border ml-3 mr-3 w-full border-black"  disabled> </textarea>
        <textarea id="darkpattern" className="h-100 border ml-3 mr-3 mt-5 w-full border-black" disabled></textarea>
      </div>
    </div>
  );
}

export default App;