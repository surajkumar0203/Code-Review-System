
import { useContext,useState,useEffect } from "react"
import { AppState } from "../App";
export default function Output() {
    const useAppState = useContext(AppState);
    const [appdata, setAppdata] = useState({
        "id":"",
        "status":"",
        "result":{
            results:[]
        }
    });
    
        const fetchData = async () => {
            if (!useAppState.token) {
                
                return;
            }
            try {
                
                const response = await fetch(`http://127.0.0.1:8002/api/task/${useAppState.token.id}/`);
                
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
    
                const data = await response.json();
                setAppdata({...data,"id":data.id,"status":data.status,"result":data.result});
                
            } catch (err) {
                console.error("Error fetching data:", err.message);
            }
           
        }
        
      
        
        
   
    return (
        <div>
        <h1 className="text-white">
        <pre>
        
            {appdata.status!=="PENDING"?(appdata.result.results[0]):appdata.status}
        
        </pre>
        </h1>
        <button onClick={fetchData} className="bg-green-800">click me</button>
        </div>
    )
}
