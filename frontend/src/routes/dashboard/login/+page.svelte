<script>
	import AuthService from '$lib/auth';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	let username = '';
	let password = '';
	let next = $page.url.searchParams.get('next') || '/';
	async function login() {
		const response = await AuthService.login(username, password);
		if (response) {
			goto(next);
		} else {
			alert('Login failed');
		}
	}
</script>

<div class="container">
	<h1 class="text-center mt-5">התחברות</h1>
	<form class="container mt-5" on:submit|preventDefault={login}>
		<div class="mb-3">
			<label for="username" class="form-label"> שם משתמש </label>
			<input
				type="text"
				class="form-control"
				id="username"
				placeholder="הכנס את שם המשתמש שלך"
				required
				bind:value={username}
			/>
		</div>
		<div class="mb-3">
			<label for="password" class="form-label"> סיסמה </label>
			<input
				type="password"
				class="form-control"
				id="password"
				placeholder="הכנס את הסיסמה שלך"
				required
				bind:value={password}
			/>
		</div>
		<button type="submit" class="btn btn-primary"> התחבר </button>
	</form>
</div>
