import Header from "./components/Header";
import Input from "./components/Input";
import Output from "./components/Output";
import { createContext } from "react";
import { useState } from "react";
import { Route, Routes } from "react-router-dom";


const AppState = createContext();
const App = () => {
  const [token, setToken] = useState({
    id:'',
    status:"",

  })
  return (
    <>
      <AppState.Provider value={{ token, setToken }}>

        <Header />
        <Routes>
          <Route path="/" element={<Input />} />
          <Route path="/output" element={<Output />} />
        </Routes>

      </AppState.Provider>
    </>
  )
}

export default App;
export { AppState };