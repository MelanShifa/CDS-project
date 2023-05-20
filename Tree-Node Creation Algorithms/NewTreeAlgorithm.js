// CDS Project
// Dawson H Rudolph
// Last Updated: 2/15/23

// fs is a Node.js module for working with the file system.
// readline is a Node.js module that provides an interface for reading data on line at a time.
const fs = require('fs');
const readline = require('readline');

// creating the courses variable which will hold the parsed data of the inputted json
let courses;

// getCourses reads using fs.readfile() the courses.json, then parses it as a json and stores
// its results in the courses variable.
const getCourses = () => {
  fs.readFile('mathCourses.json', 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    courses = JSON.parse(data);
  });
};

// calling the getCourses function
getCourses();

// color for the "AND" nodes
const colors = [
  'purple',
  'yellow',
  'black',
  'blue',
  'red',
  'green',
  'orange',
  'pink',
  'brown',
  'grey',
];

// getPrerequisites is the base recursiver function for identifying and returning the prerequisites
// of an inputted course in an array.
// Parameters:
// 1. Course: the course that the function is finding the prerequisites of.
// 2. Parent: optional parameter; the course that is the parent of the course being analyzed.
// 3. Prerequisites: optional paramter; an array of the prereqs for the given course.
// 4. Color: the node color associated with the course/courses
const getPrerequisites = (course, parent = null, prerequisites = [], color = 'purple') => {

  // if the course is not in the courses object, an error will be presented.
  if (!courses[course]) {
    console.error(`The course ${course} does not exist.`);
    return;
  }

  let colorIndex = colors.indexOf(color);

  // if the course is in the courses object:
  courses[course].forEach((prereq) => {
    if (Array.isArray(prereq)) {
      // This prereq is an array of "AND" classes, so we give it a different color
      colorIndex = (colorIndex + 1) % colors.length;
      const newColor = colors[colorIndex];

      // Process here is the same as the process below except because this is the "AND" section
      // courses need to be represented in their respective colors so we have the newColor variable
      // and the andPrereq which is the pre reqs for the "AND" classes
      prereq.forEach((andPrereq) => {
        if (!prerequisites.some(({ course: c }) => c === andPrereq)) {
          prerequisites.push({
            course: andPrereq,
            prerequisites: getPrerequisites(andPrereq, course, [], newColor),
            color: newColor,
          });
        }
      });
    } else {

      // Split the prereq into separate courses if it contains ","
      const prereqCourses = prereq.split(',').map((p) => p.trim());

      prereqCourses.forEach((prereqCourse) => {
        //  for each prereq of the current course the function checks if it is included
        //  in the prerequisites array.
        if (!prerequisites.some(({ course: c }) => c === prereqCourse)) {

          // if the course is in the prerequisites array it gets added to the array
          // and is given the three properties: course, color, prerequisites.
          prerequisites.push({
            course: prereqCourse,
            // recursive call to the getPrerequisites function
            prerequisites: getPrerequisites(prereqCourse, course, [], color),
            color: color,
          });
        }
      });
    }
  });

  // returning the prereqs
  return prerequisites;
};

// creating the readline interface.
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// rl.question is a method from the readline module, creates an interface allowing the user
// to interact with the command line.

// question method asks the user to enter the course.
rl.question('Enter a course: ', (input) => {

  // the users input is passed as input, this user input then fills the course parameter
  // and is entered into the getPrerequisites function of the prereqs parameter.
  const prerequisites = [{
    course: input,
    prerequisites: getPrerequisites(input),
    color: 'purple',
  }];

  // creating the output .json file object
  const fileName = 'prerequisites.json';

  //   fs.writeFile is called which writes the prereqs onto the file.
  //   the parameters include: filename, data to be written which is the prerequsites converted
  //   to a json by utilizing json.stringify method, and then a callback function which
  //   is executed after everything has been written.
  fs.writeFile(fileName, JSON.stringify(prerequisites, null, 2), (err) => {
    if (err) {
      console.error(err);
      return;
    }

    // console log notifying the user that the prereqs have been saved to a new json file.
    console.log(`The prerequisites for ${input} have been saved to ${fileName}.`);
  });

  // closing the readline interface
  rl.close();
});

