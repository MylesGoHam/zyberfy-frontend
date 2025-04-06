import React, { useState } from "react";
import { motion } from "framer-motion";

export default function App() {
  const [sender, setSender] = useState("");
  const [recipient, setRecipient] = useState("");
  const [tone, setTone] = useState("Professional");
  const [email, setEmail] = useState("");
  const [reply, setReply] = useState("");
  const [loading, setLoading] = useState(false);
  const [copied, setCopied] = useState(false);

  const handleGenerate = async () => {
    if (!sender || !recipient || !email) {
      setReply("Please fill in all fields.");
      return;
    }

    setLoading(true);
    try {
      const response = await fetch("/api/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ sender, recipient, tone, email }),
      });
      const data = await response.json();
      setReply(data.reply || "No reply generated.");
    } catch (error) {
      setReply("Error generating reply.");
    }
    setLoading(false);
  };

  return (
    <main className="min-h-screen bg-white text-gray-800 px-4 py-10">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
        className="max-w-2xl mx-auto"
      >
        <h1 className="text-4xl font-bold text-center mb-6 text-electric-blue">Zyberfy</h1>
        <p className="text-center text-gray-500 mb-8">AI replies tailored to your voice.</p>

        <div className="space-y-4">
          <input
            placeholder="Sender"
            value={sender}
            onChange={(e) => setSender(e.target.value)}
            className="w-full border border-gray-300 rounded-xl p-3"
          />
          <input
            placeholder="Recipient"
            value={recipient}
            onChange={(e) => setRecipient(e.target.value)}
            className="w-full border border-gray-300 rounded-xl p-3"
          />
          <select
            value={tone}
            onChange={(e) => setTone(e.target.value)}
            className="w-full border border-gray-300 rounded-xl p-3"
          >
            <option value="Professional">Professional</option>
            <option value="Friendly">Friendly</option>
            <option value="Witty">Witty</option>
          </select>
          <textarea
            placeholder="Paste the email here..."
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full border border-gray-300 rounded-xl p-3 h-32"
          />
          <button
            onClick={handleGenerate}
            disabled={loading || !sender || !recipient || !email}
            className="w-full bg-electric-blue text-white py-3 rounded-xl font-semibold transition hover:brightness-110 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {loading ? "Generating..." : "Generate Reply"}
          </button>
        </div>

        {reply && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="mt-6 p-4 bg-gray-100 border border-gray-200 rounded-xl whitespace-pre-wrap"
          >
            {reply}
            <button
              onClick={() => {
                navigator.clipboard.writeText(reply);
                setCopied(true);
                setTimeout(() => setCopied(false), 2000);
              }}
              className="mt-4 text-sm bg-electric-blue text-white px-4 py-2 rounded hover:brightness-110 transition"
            >
              {copied ? "Copied!" : "Copy to Clipboard"}
            </button>
          </motion.div>
        )}
      </motion.div>

      {/* Testimonials */}
      <section className="max-w-4xl mx-auto mt-20 px-4 border-t pt-16">
        <h2 className="text-2xl font-semibold text-center mb-8">What Others Are Saying</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {[
            {
              name: "Emma L.",
              quote: "Zyberfy cut my email time in half. It's like having a full-time assistant.",
            },
            {
              name: "James W.",
              quote: "The replies sound just like me. Super impressed with the quality.",
            },
            {
              name: "Sophia R.",
              quote: "As a small business owner, this tool is a game-changer.",
            },
          ].map((testimonial, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: i * 0.2, duration: 0.5 }}
              className="bg-white p-6 rounded-2xl shadow-md border border-gray-200"
            >
              <p className="text-gray-600 italic mb-4">“{testimonial.quote}”</p>
              <p className="font-semibold text-gray-900">— {testimonial.name}</p>
            </motion.div>
          ))}
        </div>
      </section>
    </main>
  );
}