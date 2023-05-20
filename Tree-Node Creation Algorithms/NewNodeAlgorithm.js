// CDS Project
// Dawson H Rudolph
// Last Updated: 2/15/23

// fs is a Node.js module for working with the file system.
const fs = require('fs');

// function for writing the nodes and edges to an output file.
// the function has two parameters which are the file paths for the input and output files.
function createNodesAndEdgesFromFileAndWriteToFile(inputFilePath, outputFilePath) {

  // creating a new promise object which is an object used to asynchrounously prodce a value.
  return new Promise((resolve, reject) => {

    // reading the inputfile and returning the contents into the data variable.
    fs.readFile(inputFilePath, 'utf-8', (err, data) => {
      // checking for errors reading the file.
      if (err) {
        reject(err);
      } else {

        // calling the function that creates nodes and edges with out parsed data.
        let nodesAndEdges = createNodesAndEdges(JSON.parse(data));

        // using the writefile method to write the contents of our nodesAndEdges variable to our output file.
        fs.writeFile(outputFilePath, JSON.stringify(nodesAndEdges, null, 2), { flag: 'w' }, (err) => {

          // checking for errors writing the file.
          if (err) {
            reject(err);
          } else {
            resolve();
          }
        });
      }
    });
  });
}

// function to create our nodes and edges.
function createNodesAndEdges(data) {
  // initializing variables
  let nodes = []; // storing node objects
  let edges = []; // storing edge objects
  let nextNodeKey = 0; // counter for node keys
  let nextEdgeKey = 0; // counter for edge keys
  
  // internal helper function that will recursively traverse the data and create the nodes and edges
  // for the prereqs.
  // contains two parameters: coursdata for the data, parentkey for the key of the parent node
  // and then x & y for the node coordinates.
  function addNodesAndEdges(courseData, parentKey, x, y) {

    // creating a key for the node by concatenating the parent key and next node key.
    let key = parentKey + '.' + nextNodeKey++;
    // adding nodes to node array with proper formation and attributes.
    nodes.push({
      "key": key,
      "attributes": {
        "x": x,
        "y": y,
        "size": 1,
        "label": courseData.course,
        "color": courseData.color || "#333"
      }
    });

    // creating the edges that connect the new node to its parent node.
    // adding edges to edge array with proper formation and attributes.
    if (parentKey) {
      edges.push({
        "key": nextEdgeKey++,
        "source": key,
        "target": parentKey,
        "attributes": {
          "size": 1
        }
      });
    }

    
    // looping through all the pre requisites and adding them to tthr prereq object
    if (courseData.prerequisites) {
      for (let i = 0; i < courseData.prerequisites.length; i++) {
        let prereq = courseData.prerequisites[i];

        // calculating the coordinates of each prereq node stemming from the
        // initial node and its prereqs.
        let prereqX = x + (i - (courseData.prerequisites.length - 1) / 2) * 5;
        let prereqY = y - 5;
        // called with the created data for the prereq, key and coordinates
        addNodesAndEdges(prereq, key, prereqX, prereqY);
      }
    }
  }
  
  // returning the nodes and edges inside their respective arrays
  addNodesAndEdges(data[0], '', 0, 0);
  return { "nodes": nodes, "edges": edges };
}

// calling our function
createNodesAndEdgesFromFileAndWriteToFile('prerequisites.json', 'output.json')
  // called after the promised is resolved and produces a message for the user
  .then(() => console.log('Nodes and edges written to file successfully!'))
  // catch for errors
  .catch(err => console.error(err));
