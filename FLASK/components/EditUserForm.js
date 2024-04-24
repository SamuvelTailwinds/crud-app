import React, { useState, useEffect } from 'react';
import { useHistory, useParams } from 'react-router-dom';
import axios from 'axios';

function EditUserForm() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const { id } = useParams();
  const history = useHistory();

  useEffect(() => {
    fetchUser();
  }, []);

  const fetchUser = async () => {
    const response = await axios.get(`http://4.240.70.99:5000/users/${id}`);
    const user = response.data;
    setName(user.name);
    setEmail(user.email);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.put(`http://4.240.70.99:5000/updateUser/${id}`, { name });
    history.push('/');
  };

  return (
    <div>
      <h2>Edit User</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Name" value={name} onChange={(e) => setName(e.target.value)} />
        <input type="email" placeholder="Email" value={email} readOnly />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default EditUserForm;
