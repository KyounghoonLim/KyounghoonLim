import logo from './logo.svg';
import { Route, Routes } from 'react-router-dom'
import TextInput from './pages/TextInput'
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
      <Routes>
        <Route path='' element={<TextInput/>} />
      </Routes>
    </div>
  );
}

export default App;
