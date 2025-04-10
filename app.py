<form action="/" method="POST" class="max-w-lg mx-auto bg-white p-6 rounded shadow-md">
  <div class="mb-4">
      <label for="name" class="block text-gray-700 font-medium mb-2">Name</label>
      <input type="text" id="name" name="name" class="w-full p-2 border border-gray-300 rounded" required />
  </div>

  <div class="mb-4">
      <label for="email" class="block text-gray-700 font-medium mb-2">Email</label>
      <input type="email" id="email" name="email" class="w-full p-2 border border-gray-300 rounded" required />
  </div>

  <div class="mb-4">
      <label for="service" class="block text-gray-700 font-medium mb-2">Service Type</label>
      <select id="service" name="service" class="w-full p-2 border border-gray-300 rounded">
          <option value="luxury-travel">Luxury Travel</option>
          <option value="event-planning">Event Planning</option>
          <option value="yacht-charter">Yacht Charter</option>
          <option value="interior-design">Interior Design</option>
          <option value="other">Other</option>
      </select>
  </div>

  <div class="mb-4">
      <label for="budget" class="block text-gray-700 font-medium mb-2">Budget</label>
      <input type="number" id="budget" name="budget" class="w-full p-2 border border-gray-300 rounded" placeholder="$10,000" required step="0.01" />
  </div>

  <div class="mb-4">
      <label for="location" class="block text-gray-700 font-medium mb-2">Location</label>
      <input type="text" id="location" name="location" class="w-full p-2 border border-gray-300 rounded" placeholder="City, Country" />
  </div>

  <div class="mb-4">
      <label for="requests" class="block text-gray-700 font-medium mb-2">Special Requests</label>
      <textarea id="requests" name="requests" class="w-full p-2 border border-gray-300 rounded" rows="4"></textarea>
  </div>

  <button type="submit" class="w-full bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700">
      Submit Proposal
  </button>
</form>
