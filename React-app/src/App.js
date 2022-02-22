import logo from './logo.svg';
import './App.css';
import Login from './Login';

/**
 1. component 
 2. props
 3. state
 4. connditional rendering
 5. control component
 6. reusable component
 */
function App() {
  return (
    <div className="App">
     <Login name="arpit" age="28"/>
    
    </div>
  );
}

export default App;
