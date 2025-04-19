const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const path = require('path');

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.static(__dirname));

// MongoDB connection with better error handling
mongoose.connect('mongodb://127.0.0.1:27017/chatbot', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    serverSelectionTimeoutMS: 5000,
    socketTimeoutMS: 45000,
})
.then(() => {
    console.log('✅ Connected to MongoDB successfully!');
    console.log('📁 Database: chatbot');
    console.log('🔌 MongoDB Port: 27017');
})
.catch(err => {
    console.error('❌ MongoDB connection error:', err);
    process.exit(1);  // Exit if MongoDB connection fails
});

// Message schema
const messageSchema = new mongoose.Schema({
  sender: String,
  text: String,
  timestamp: { type: Date, default: Date.now }
});

const Message = mongoose.model('Message', messageSchema);

// Save message API
app.post('/api/messages', async (req, res) => {
  try {
    console.log('📥 Received message:', req.body);
    const message = new Message(req.body);
    await message.save();
    console.log('💾 Message saved successfully!');
    res.status(201).json({ success: true });
  } catch (err) {
    console.error('❌ Error saving message:', err);
    res.status(500).json({ error: 'Failed to save message' });
  }
});

// Get all messages API
app.get('/api/messages', async (req, res) => {
  try {
    const messages = await Message.find().sort({ timestamp: 1 });
    console.log('📤 Retrieved messages:', messages);
    res.json(messages);
  } catch (err) {
    console.error('❌ Error getting messages:', err);
    res.status(500).json({ error: 'Failed to get messages' });
  }
});

// Serve static files
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(3000, () => {
    console.log('🚀 Server running on http://localhost:3000');
});