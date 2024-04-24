import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

function UserList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    const response = await axios.get('http://4.240.70.99:5000/users');
    setUsers(response.data);
  };

  const deleteUser = async (id) => {
    await axios.delete(`http://4.240.70.99:5000/deleteUser/${id}`);
    fetchUsers();
  };

  return (
    <div>
      <h2>Users</h2>
      <ul>
        {users.map((user) => (
          <li key={user._id}>
            {user.name} - {user.email}
            <Link to={`/edit/${user._id}`}>Edit</Link>
            <button onClick={() => deleteUser(user._id)}>Delete</button>
          </li>
        ))}
      </ul>
      <Link to="/add">Add User</Link>
    </div>
  );
}

export default UserList;
