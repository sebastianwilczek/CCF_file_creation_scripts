const [REDACTED] = require('[REDACTED]');
const cheerio = require('cheerio');
const afterLoad = require('after-load');
const http = require('http');
const fs = require('fs');
const crypto = require("crypto");

(async () => {
  try {
  	const urlString = await [REDACTED].mirror();
  	console.log(`${urlString} is currently fastest`);
	iterateDownload(urlString);
    return true;
  } catch(err) {
      return console.dir(err);
  }
})();

function iterateDownload(downloadMirror) {
  downloadRandom(downloadMirror);
}

function downloadRandom(downloadMirror) {
  (async () => {
    const options = {
      mirror: downloadMirror,
      count: 10,
      fields: [{extension:"pdf"}]
    }
    try {
      while(true) {
        const data = await [REDACTED].random.text(options);
        let n = data.length;
        console.log(n + " random PDFs with titles");
        while (n--) {
          var downloadLink = '[REDACTED]' + data[n].md5.toLowerCase();
          console.log('Working link: ' + downloadLink);
          getFromDownloadPage(downloadLink);
        }
      }
      return true;
    } catch (err) {
      console.error(err);
    }
  })();
}

function getFromDownloadPage(downloadURL) {
  afterLoad(downloadURL, function(html){
    const $ = cheerio.load(html);
    links = $('a'); //jquery get all hyperlinks
    $(links).each(function(i, link){
      var link = $(link).attr('href');
      if(link.endsWith('pdf')) {
      	var linkToDownload = '[REDACTED]' + link;
      	var id = crypto.randomBytes(10).toString('hex');
      	console.log(linkToDownload + ' ==> ' + id + '.pdf');
      	const file = fs.createWriteStream(id + '.pdf');
		const request = http.get(linkToDownload, function(response) {
		  response.pipe(file);
		});
      }
    });
  });
}
