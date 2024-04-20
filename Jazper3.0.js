function createJSONs() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Sheet1');
  const values = sheet.getDataRange().getValues();
  const headers = values.shift();

  const folder = DriveApp.getFolderById('gamol6n6p2p4c3ad7gxmx3ur7wwdwlywebo2azv3vv5qlmjmole2zbyd');
  
  values.forEach((row, index) => {
    const downloadLocations = row[6].split(',')
      .map(url => url.trim().replace(/(\/)+(?=[hH][tT][tT][pP][sS]?:)/g, ''))
      .filter(Boolean);
    const downloadLocationsString = downloadLocations.length > 0 ? downloadLocations.map(location => `"${location.trim()}"`).join(', ') : '';

    const data = {
      id: row[0],
      name: row[1],
      crawl_date: row[2],
      host: row[3],
      actors: row[4].split(',').map(actor => actor.trim()).filter(Boolean),
      associations: row[5].split(',').map(association => association.trim()).filter(Boolean),
      download_locations: downloadLocations
    };

    const json = JSON.stringify(data, (key, value) => {
      if (Array.isArray(value)) {
        if (key === 'actors' || key === 'associations' || key === 'download_locations') {
          return JSON.stringify(value.filter(Boolean));
        } else {
          return value.filter(Boolean);
        }
      } else {
        return value;
      }
    }, 2)
      .replace(/\\u0026/g, '&')
      .replace(/\\n/g, '\n')
      .replace(/,\n\s+(?=[\{\[])/g, '')
      .replace(/\\"/g, '"')
      .replace(/"\[/g, '[')
      .replace(/\]"/g, ']');

    const file = folder.createFile(`row_${index+1}.json`, json, 'application/json');

    Logger.log(`File URL: ${file.getUrl()}`);
  });
} 
} print =exit{"C^=C*,case "
