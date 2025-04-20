const domOutput = document.getElementById("todo-output");
const todoInput = document.getElementById("todo-input");
function loadTodos() {
    const todos = JSON.parse(localStorage.getItem('todos')) || [];
    todos.forEach(todo => {
        addTodoToDOM(todo.text, todo.completed);
    });
}
function saveTodos() {
    const todos = [];
    domOutput.querySelectorAll('.todo-item').forEach(item => {
        todos.push({
            text: item.querySelector('span').innerText,
            completed: item.classList.contains('line-through')
        });
    });
    localStorage.setItem('todos', JSON.stringify(todos));
}
function addTodoToDOM(text, completed = false) {
    const newItem = document.createElement("div");
    newItem.className = `todo-item flex justify-between items-center p-2 mb-2 bg-black p-6 rounded ${completed ? 'line-through' : ''}`;
    newItem.innerHTML = `
        <span>${text}</span>
        <div>
            <button class="complete-btn bg-green-500 text-black px-2 py-1 rounded hover:bg-green-600 mr-2">${completed ? 'Batal' : 'Selesai'}</button>
            <button class="delete-btn bg-red-500 text-black px-2 py-1 rounded hover:bg-red-600">Hapus</button>
        </div>
    `;
    domOutput.appendChild(newItem);

    newItem.querySelector('.complete-btn').addEventListener('click', function () {
        newItem.classList.toggle('line-through');
        this.innerText = newItem.classList.contains('line-through') ? 'Batal' : 'Selesai';
        saveTodos();
    });

    newItem.querySelector('.delete-btn').addEventListener('click', function () {
        domOutput.removeChild(newItem);
        saveTodos();
    });
}

document.getElementById("btn-tambah-item").addEventListener("click", function () {
    const text = todoInput.value.trim();
    if (text !== "") {
        addTodoToDOM(text);
        todoInput.value = "";
        saveTodos();
    }
});

loadTodos();
function hitungKalkulator(angka1, angka2, operasi) {
    let hasil = 0;
    switch (operasi) {
        case "tambah":
            hasil = angka1 + angka2;
            break;
        case "kurang":
            hasil = angka1 - angka2;
            break;
        case "kali":
            hasil = angka1 * angka2;
            break;
        case "bagi":
            if (angka2 === 0) {
                return "Error: Pembagian dengan nol tidak diperbolehkan";
            }
            hasil = angka1 / angka2;
            break;
        case "pangkat":
            hasil = Math.pow(angka1, angka2);
            break;
        case "akar":
            if (angka1 < 0) {
                return "Error: Akar kuadrat dari bilangan negatif tidak diperbolehkan";
            }
            hasil = Math.sqrt(angka1);
            break;
        case "modulus":
            if (angka2 === 0) {
                return "Error: Modulus dengan nol tidak diperbolehkan";
            }
            hasil = angka1 % angka2;
            break;
        default:
            return "Operasi tidak valid";
    }
    return hasil;
}

function tampilkanHasil(angka1, angka2, operasi, simbol) {
    const hasilElement = document.getElementById("hasil-kalkulator");
    if (isNaN(angka1) || isNaN(angka2)) {
        hasilElement.innerHTML = `<p class="text-red-500">Masukkan angka yang valid!</p>`;
    } else {
        const hasil = hitungKalkulator(angka1, angka2, operasi);
        if (typeof hasil === "string") {
            hasilElement.innerHTML = `<p class="text-red-500">${hasil}</p>`;
        } else {
            hasilElement.innerHTML = `<p>Hasil: ${angka1} ${simbol} ${angka2} = ${hasil}</p>`;
        }
    }
}

document.getElementById("btn-tambah").addEventListener("click", function () {
    const angka1 = parseFloat(document.getElementById("angka1").value);
    const angka2 = parseFloat(document.getElementById("angka2").value);
    tampilkanHasil(angka1, angka2, "tambah", "+");
});

document.getElementById("btn-kurang").addEventListener("click", function () {
    const angka1 = parseFloat(document.getElementById("angka1").value);
    const angka2 = parseFloat(document.getElementById("angka2").value);
    tampilkanHasil(angka1, angka2, "kurang", "-");
});

document.getElementById("btn-kali").addEventListener("click", function () {
    const angka1 = parseFloat(document.getElementById("angka1").value);
    const angka2 = parseFloat(document.getElementById("angka2").value);
    tampilkanHasil(angka1, angka2, "kali", "×");
});

document.getElementById("btn-bagi").addEventListener("click", function () {
    const angka1 = parseFloat(document.getElementById("angka1").value);
    const angka2 = parseFloat(document.getElementById("angka2").value);
    tampilkanHasil(angka1, angka2, "bagi", "÷");
});

document.getElementById("btn-pangkat").addEventListener("click", function () {
    const angka1 = parseFloat(document.getElementById("angka1").value);
    const angka2 = parseFloat(document.getElementById("angka2").value);
    tampilkanHasil(angka1, angka2, "pangkat", "^");
});

document.getElementById("btn-akar").addEventListener("click", function () {
    const angka1 = parseFloat(document.getElementById("angka1").value);
    const angka2 = 0; // Tidak digunakan untuk akar kuadrat
    tampilkanHasil(angka1, angka2, "akar", "√");
});

document.getElementById("btn-modulus").addEventListener("click", function () {
    const angka1 = parseFloat(document.getElementById("angka1").value);
    const angka2 = parseFloat(document.getElementById("angka2").value);
    tampilkanHasil(angka1, angka2, "modulus", "%");
});

function validasiForm(event) {
    event.preventDefault(); // Mencegah form submit

    const nama = document.getElementById("nama").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();

    document.getElementById("error-nama").textContent = "";
    document.getElementById("error-email").textContent = "";
    document.getElementById("error-password").textContent = "";

    if (nama.length <= 3) {
        document.getElementById("error-nama").textContent = "Nama harus lebih dari 3 karakter.";
        return;
    }

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        document.getElementById("error-email").textContent = "Email tidak valid.";
        return;
    }

    if (password.length < 8) {
        document.getElementById("error-password").textContent = "Password harus minimal 8 karakter.";
        return;
    }

    alert("Form berhasil divalidasi dan siap disubmit!");
}

document.getElementById("form-validasi").addEventListener("submit", validasiForm);