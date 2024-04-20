function createJSONs() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Sheet1');
  const values = sheet.getDataRange().getValues();
  const headers = values.shift();

  const folder = DriveApp.getFolderById('1SV9zxU1DizBfY7i7iz6nhS8oytkNSCAX');
  
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
    const fileUrl = file.getUrl();

    // Add the Drive link to the spreadsheet
    const rowRange = sheet.getRange(index + 2, 8); // Assuming Drive links will be added in column G (7th column)
    rowRange.setValue(fileUrl);

    Logger.log(`File URL: ${fileUrl}`);
  });
}
