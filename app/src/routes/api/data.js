// src/routes/api/data.js
import { exec } from 'child_process';

export async function get() {
  // Execute the Python script to generate random numbers
  const { stdout, stderr } = await new Promise((resolve) => {
    exec('python ../python_scripts/random_numbers.py', (error, stdout, stderr) => {
      resolve({ stdout, stderr });
    });
  });

  if (stderr) {
    console.error('Error occurred while executing the Python script:', stderr);
    return {
      status: 500,
      body: { error: 'Internal server error' }
    };
  }

  let data = [];

  try {
    data = JSON.parse(stdout);
  } catch (error) {
    console.error('Error parsing JSON data from Python script:', error);
    return {
      status: 500,
      body: { error: 'Internal server error' }
    };
  }

  // Return the data as JSON
  return {
    body: data
  };
}
