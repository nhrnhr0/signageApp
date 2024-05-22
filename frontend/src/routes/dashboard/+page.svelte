<script>
	import AuthService from '$lib/auth';
	import { page } from '$app/stores';
	AuthService.protected_route();
</script>

<div class="container mt-5">
	<ul>
		<li><a href="{$page.url.origin}{$page.url.pathname}/playlists">פלייליסטים</a></li>
		<li><a href="{$page.url.origin}{$page.url.pathname}/screens">מסכים</a></li>
	</ul>
</div>
