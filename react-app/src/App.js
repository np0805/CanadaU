/*
import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
*/


/*
import React from 'react';

function App() {
  return <p>Hello world!</p>;
}

export default App;
*/

/*
import React from 'react';


// Import our styles.
import './App.css';

function App() {
  // Here `className` is only used for styling.
  return <div className="App">Hello world!</div>;
}

export default App;
*/

/*
import React from 'react';

import './App.css';

function App() {
  // NOTE: className is only used for styling.
  return (
    <div className="App">
      <h1>uWaterloo</h1>
      <p>Subscribers: 44000</p>
    </div>
  );
}

export default App;
*/

/*
import React from 'react';

import './App.css';

function App() {
  // NOTE: className is only used for styling.
  return (
    <div className="App">
      <h1>uWaterloo</h1>
      <p>Subscribers: 44000</p>
    </div>
  );
}

function Subreddit(props) {
  return (
    <div className="Subreddit">
      <h1>{props.displayName}</h1>
      <p>Subscribers: {props.subscribers}</p>
    </div>
  );
}
export default App;
*/

/*
import React from 'react';

import './App.css';
function App(props) {
  const subreddits = [
    // Subreddit 1
    {
      displayName: 'uwaterloo',
      subscribers: 44444,
      icon:
        'https://a.thumbs.redditmedia.com/c1iqtotu4lNlCxkJBex6SEtlikJBqt6WmKBNgMQKjS0.png'
    },
    // Subreddit 2
    {
      displayName: 'UofT',
      subscribers: 3,
      icon:
        'https://a.thumbs.redditmedia.com/SsZbo9uA8c68Lhc68dk59PuZkjm_gnxNBx2e14haVY8.png'
    }
  ];

  // NOTE: the map function loops over all the data.
  return (
    <div className="App">
      {subreddits.map((subreddit, i) => (
        <Subreddit
          key={i}
          displayName={subreddit.displayName}
          subscribers={subreddit.subscribers}
        />
      ))}
    </div>
  );
}

export default App;
*/


import React, { useState } from 'react';

import WordCloud from 'react-d3-cloud';

import './App.css';

function App(props) {
  const subreddits = [
    {
      displayName: 'uwaterloo',
      subscribers: 44444,
      icon:
        'https://a.thumbs.redditmedia.com/c1iqtotu4lNlCxkJBex6SEtlikJBqt6WmKBNgMQKjS0.png',
      wordCounts: [
        { text: 'day', value: 42 },
        { text: 'busan', value: 23 },
        { text: 'waterloo', value: 20 },
        { text: 'uw', value: 19 },
        { text: 'uwaterloo', value: 18 },
        { text: 'week', value: 18 },
        { text: 'like', value: 17 },
        { text: 'goose', value: 15 },
        { text: 'people', value: 15 },
        { text: 'students', value: 13 },
        { text: 'today', value: 12 },
        { text: 'year', value: 11 }
      ]
    },
    {
      displayName: 'UofT',
      subscribers: 3,
      icon:
        'https://a.thumbs.redditmedia.com/SsZbo9uA8c68Lhc68dk59PuZkjm_gnxNBx2e14haVY8.png',
      wordCounts: [
        { text: 'uoft', value: 38 },
        { text: 'exam', value: 17 },
        { text: 'like', value: 15 },
        { text: 'people', value: 15 },
        { text: 'test', value: 15 },
        { text: 'today', value: 13 },
        { text: 'course', value: 12 },
        { text: 'campus', value: 11 },
        { text: 'year', value: 11 },
        { text: 'students', value: 10 },
        { text: 'bad', value: 10 }
      ]
    }
  ];

  return (
    <div className="App">
      <h1 className="App-title">CanadaU</h1>
      {subreddits.map((subreddit, i) => (
        <Subreddit
          key={i}
          displayName={subreddit.displayName}
          subscribers={subreddit.subscribers}
          icon={subreddit.icon}
          wordCounts={subreddit.wordCounts}
        />
      ))}
    </div>
  );
}

function Subreddit(props) {
  const fontSizeMapper = word => word.value * 2;

  const [isFavourite, setFavourite] = useState(false);

  return (
    <div className="Subreddit" onClick={() => setFavourite(true)}>
      <img className="Subreddit-icon" src={props.icon} />
      <div className="Subreddit-summary">
        <h1>{props.displayName}</h1>
        <p>Subscribers: {props.subscribers}</p>
        {isFavourite ? <p>Favourited!</p> : null}
      </div>
      <WordCloud
        data={props.wordCounts}
        fontSizeMapper={fontSizeMapper}
        width={300}
        height={300}
      />
    </div>
  );
}

export default App;