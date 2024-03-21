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
			<li class="nav-item active">
				<a class="nav-link" href="/">בית <span class="sr-only">(current)</span></a>
			</li>
			<li class="nav-item">
				<a class="nav-link" href="/playlists"> פלייליסטים </a>
			</li>
			<li class="nav-item">
				<a class="nav-link" href="/screens"> מסכים </a>
			</li>

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
					<a class="nav-link" href="/login">Login</a>
				</li>
			{/if}
		</ul>
	</div>
</nav>
