import { useState} from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

export default function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const { register } = useAuth() 
    const navigate = useNavigate();
    

    
    const handleSubmit = (e) => {
        e.preventDefault();
        if (register(username, password)) {
            alert("Login successful")
            navigate("/")
        } else {
            alert("Incorrect data")
            
        }
    };
    

    return (
        <form onSubmit={handleSubmit}>
            <h2>Login</h2>
            <input placeholder="Username" type="text" value={username} onChange={(e) => setUsername(e.target.value)} required />
            <input placeholder="Password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
            <button type="submit">Login</button>
        </form>
    )
}