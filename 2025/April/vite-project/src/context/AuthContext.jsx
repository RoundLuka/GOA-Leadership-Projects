import { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

const adminData = {
    username: "admin",
    password: "admin123",
    role: "admin",
};

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);

    useEffect(() => {
        const stored = localStorage.getItem("currentUser");
        if (stored) {
            setUser(JSON.parse(stored));
        }
    }, []);

    const login = (username, password) => {
        if (username === adminData.username && password === adminData.password) {
            setUser(adminData);
            localStorage.setItem("currentUser", JSON.stringify(adminData));
            return true;
        }

        const users = JSON.parse(localStorage.getItem("users")) || [];
        for (let i = 0; i < users.length; i++) {
            const current = users[i];
            if (current.username === username && current.password === password) {
                setUser(current);
                localStorage.setItem("currentUser", JSON.stringify(current));
                return true;
            }
        }

        return false;
    };

    const register = (username, password) => {
        const users = JSON.parse(localStorage.getItem("users")) || [];

        for (let i = 0; i < users.length; i++) {
            const current = users[i];
            if (current.username === username) {
                return false;
            }
        }

        const newUser = { username, password, role: "user" };
        users.push(newUser);
        localStorage.setItem("users", JSON.stringify(users));
        return true;
    };

    const logout = () => {
        setUser(null);
        localStorage.removeItem("currentUser");
    };

    return (
        <AuthContext.Provider value={{ user, login, register, logout }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => {
    return useContext(AuthContext);
};
