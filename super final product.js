function createJSONs() {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Sheet1');
    const values = sheet.getDataRange().getValues();
    const headers = values.shift();
  
    values.forEach((row, index) => {
  
      const data = {
        id: row[0],
        name: row[1],
        crawl_date: row[2],
        host: row[3],
        actors: row[4].split(','),
        associations: row[5].replace(/[\/\\]/g, '').split(','),
        download_locations: row[6].replace(/[\/\\]/g, '').split(',')
      };
      
      // Join actors and associations into a single line
      data.actors = data.actors.join(', ');
      data.associations = data.associations.join(', ');
  
      const json = JSON.stringify(data, null, 2)
                     .replace(/\\u0026/g, '&')
                     .replace(/\\n/g, '\n')
                     .replace(/,\n\s+(?=[\{\[])/g, '');
  
      const file = DriveApp.createFile(`row_${index+1}.json`, json, 'application/json');
  
      Logger.log(`File URL: ${file.getUrl()}`);
    });
  }