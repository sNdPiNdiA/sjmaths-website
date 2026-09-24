const HOST = 'sjmaths.com';
const KEY = 'c4b18f8e02d849bfa4876b5d9284210e';
const KEY_LOCATION = `https://${HOST}/${KEY}.txt`;

// Dead / deprecated / redirected URLs to inform IndexNow engines (Bing / Yandex)
const deadUrls = [
  `https://${HOST}/export.txt`,
  `https://${HOST}/classes/live-class.html`,
  `https://${HOST}/classes/`,
  `https://${HOST}/classes`
];

async function submitDeadLinks() {
  const payload = {
    host: HOST,
    key: KEY,
    keyLocation: KEY_LOCATION,
    urlList: deadUrls
  };

  try {
    const response = await fetch('https://api.indexnow.org/indexnow', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json; charset=utf-8' },
      body: JSON.stringify(payload)
    });
    console.log(`IndexNow Dead Link Notification (${deadUrls.length} URLs): Status ${response.status} ${response.statusText}`);
  } catch (err) {
    console.error('Error notifying IndexNow of dead links:', err.message);
  }
}

submitDeadLinks();
