// File: zyberfy-frontend/src/App.js

import React from 'react';

export default function App() {
  return (
    <div className="min-h-screen bg-gray-950 text-white px-4">
      {/* Header */}
      <header className="text-center py-12">
        <h1 className="text-4xl font-extrabold text-electric-blue mb-4">Zyberfy</h1>
        <p className="text-xl font-medium">Reply without replying.</p>
        <p className="text-lg text-gray-300 mt-2">Smart email replies tailored to your voice.</p>
      </header>

      {/* Features */}
      <section className="max-w-3xl mx-auto py-10">
        <h2 className="text-2xl font-semibold mb-4">Features</h2>
        <ul className="list-disc list-inside space-y-2">
          <li>AI-Powered Smart Email Replies</li>
          <li>Dynamic & Personalized Templates</li>
          <li>Robust Analytics & Reporting</li>
          <li>Seamless Integration with Existing Tools</li>
        </ul>
      </section>

      {/* How It Works */}
      <section className="max-w-3xl mx-auto py-10">
        <h2 className="text-2xl font-semibold mb-4">How It Works</h2>
        <ol className="list-decimal list-inside space-y-2">
          <li>Connect your inbox securely</li>
          <li>Choose your tone and preferences</li>
          <li>Let Zyberfy draft and send replies</li>
        </ol>
      </section>

      {/* CTA */}
      <section className="text-center py-10">
        <h2 className="text-xl font-semibold mb-2">Emails piling up?</h2>
        <p className="text-gray-300 mb-4">Take back your time with Zyberfy.</p>
        <a
          href="#"
          className="inline-block bg-electric-blue text-black px-6 py-3 rounded-2xl font-semibold hover:brightness-110 transition"
        >
          Join the Waitlist
        </a>
      </section>

      {/* Footer */}
      <footer className="text-center py-6 text-gray-500 border-t border-gray-800">
        © Zyberfy 2025. All rights reserved.
      </footer>
    </div>
  );
}
