import { useContext,useState } from "react"
import { AppState } from "../App";
export default function Body() {
    const useAppState = useContext(AppState);
    const [form,setForm] = useState({
        github_url: "",
        pr_number: "",
        github_token: "",
    });

    const [loading,setLoading]=useState(0);

    const handlerSubmit = async(event) =>{
        event.preventDefault();
        const {github_url,pr_number,github_token} = form;
        const url = "http://127.0.0.1:8002/api/task/";
        try{
            setLoading(1)
            const response = await fetch(url,{
                method: "POST",
                headers: {
                    'Content-Type': 'application/json' 
                },
                body: JSON.stringify({
                    "url":github_url,
                    "pr_number":pr_number,
                    "github_token":github_token
                })
            })
            setLoading(0)
            if (response.status === 200) {
                let data = await response.json();
                useAppState.setToken({"id": data.id, "status": data.status});
             
            } else {
                throw 'Error fetching users list'
            }
        }catch(e){
            setLoading(0)
            console.error('Fetch error:', error);
        }
        

    }


    return (
        <div className="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
            <div className="sm:mx-auto sm:w-full sm:max-w-sm">
                    <h2 className="mt-10 text-center text-2xl/9 font-bold tracking-tight text-white">Code Review System</h2>
            </div>

            <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
                <form className="space-y-6" action="#" onSubmit={handlerSubmit} method="POST">
                    <div>
                        <label htmlFor="github_url" className="block text-sm/6 font-medium text-white">Github url</label>
                        <div className="mt-2">
                            <input id="github_url" name="github_url" type="text" required className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-green-600 sm:text-sm/6 px-2" placeholder="Type or pase your github url"
                                value={form.github_url}
                                onChange={(e) => setForm({ ...form, github_url: e.target.value })}

                            />
                        </div>
                    </div>

                    <div>
                        <div className="flex items-center justify-between">
                            <label htmlFor="pr_number" className="block text-sm/6 font-medium text-white">Pr number</label>
                        </div>
                        <div className="mt-2">
                            <input id="pr_number" name="pr_number" type="number"  required className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-green-600 sm:text-sm/6 px-2" placeholder="Type or pase your pr_number"
                                value={form.pr_number}
                                onChange={(e) => setForm({ ...form, pr_number: e.target.value })}
                            />
                        </div>
                    </div>
                    <div>
                        <div className="flex items-center justify-between">
                            <label htmlFor="github_token" className="block text-sm/6 font-medium text-white">Github token</label>
                        </div>
                        <div className="mt-2">
                            <input id="github_token" name="github_token" type="text"  className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-green-600 sm:text-sm/6 px-2" placeholder="Type or pase your github token"
                                value={form.github_token}
                                onChange={(e) => setForm({ ...form, github_token: e.target.value })}
                            />
                        </div>
                    </div>

                    <div>
                        <button type="submit" className="flex w-full justify-center rounded-md bg-green-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-sm hover:bg-green-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-green-600">{loading?'Wait...':"Send"}</button>
                    </div>
                </form>

                
            </div>
        </div>
    )
}
