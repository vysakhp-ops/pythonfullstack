export async function getItems() {
    const res = await fetch("/api/items");
    return res.json();
}

export async function addItem(name) {
    return await fetch("/api/items?name=" + name, { method: "POST" });
}
