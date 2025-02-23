document.addEventListener('DOMContentLoaded', function () {
  // Fetch Quote One using the proxy endpoint
  fetch('/proxy/zenquotes/')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok: ' + response.statusText);
      }
      return response.json();
    })
    .then(data => {
      // data is an array with one object from ZenQuotes
      const quote = data[0];
      document.getElementById('quoteOne').innerHTML = quote.q;
      document.getElementById('quoteOneAuthor').innerHTML = quote.a;
    })
    .catch(error => {
      console.error('Error fetching quote one:', error);
      document.getElementById('quoteOne').innerHTML = "Sorry, no quote available.";
    });

  // Fetch Quote Two using the proxy endpoint
  fetch('/proxy/zenquotes/')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok: ' + response.statusText);
      }
      return response.json();
    })
    .then(data => {
      const quote = data[0];
      document.getElementById('quoteTwo').innerHTML = quote.q;
      document.getElementById('quoteTwoAuthor').innerHTML = quote.a;
    })
    .catch(error => {
      console.error('Error fetching quote two:', error);
      document.getElementById('quoteTwo').innerHTML = "Sorry, no quote available.";
    });

  // Fetch Quote Three using the proxy endpoint
  fetch('/proxy/zenquotes/')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok: ' + response.statusText);
      }
      return response.json();
    })
    .then(data => {
      const quote = data[0];
      document.getElementById('quoteThree').innerHTML = quote.q;
      document.getElementById('quoteThreeAuthor').innerHTML = quote.a;
    })
    .catch(error => {
      console.error('Error fetching quote three:', error);
      document.getElementById('quoteThree').innerHTML = "Sorry, no quote available.";
    });
});
