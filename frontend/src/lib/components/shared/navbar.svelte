<script>
	import { page } from '$app/stores';
	import AuthService, { isLoggedIn } from '$lib/auth';
</script>

<nav class="navbar navbar-expand-lg navbar-light bg-light">
	<a class="navbar-brand" href="#">
		<img src="/logo-black.png" width="30" height="30" class="d-inline-block align-top" alt="" />
	</a>
	<button
		class="navbar-toggler"
		type="button"
		data-toggle="collapse"
		data-target="#navbarNav"
		aria-controls="navbarNav"
		aria-expanded="false"
		aria-label="Toggle navigation"
	>
		<span class="navbar-toggler-icon"></span>
	</button>
	<div class="collapse navbar-collapse" id="navbarNav">
		<ul
			class="navbar-nav
        "
		>
			<li class="nav-item" class:active={$page.url === '/dashboard'}>
				<a class="nav-link" href="/dashboard">בית <span class="sr-only">(current)</span></a>
			</li>
			<li class="nav-item" class:active={$page.url.toString().includes('/dashboard/playlists')}>
				<a class="nav-link" href="/dashboard/playlists"> פלייליסטים </a>
			</li>
			<li class="nav-item" class:active={$page.url.toString().includes('/dashboard/screens')}>
				<a class="nav-link" href="/dashboard/screens"> מסכים </a>
			</li>
		</ul>
	</div>

	<ul class="navbar-nav ml-auto">
		{#if $isLoggedIn}
			<li class="nav-item">
				<a
					class="nav-link"
					href="#"
					on:click|preventDefault={() => {
						AuthService.logout();
						window.location.reload();
					}}>Logout</a
				>
			</li>
		{:else}
			<li class="nav-item">
				<a class="nav-link" href="/dashboead/login">Login</a>
			</li>
		{/if}
	</ul>
</nav>
