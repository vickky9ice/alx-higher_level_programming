#!/usr/bin/node
if (process.argv.length < 1) {
  console.log('No argument');
} else if (process.argv.length < 2) {
    console.log('Arguments found');
  } else {
    console.log('Argument found');
  }
